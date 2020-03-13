import io

from blog.models import User
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from xlwt import Workbook
import xlrd


def exportUserExcel(request):
    """
    导出excel表格
    """
    list_obj = User.objects.all().order_by("id")
    if list_obj:
        # 创建工作薄
        wb = Workbook(encoding='utf-8')
        w = wb.add_sheet(u"数据报表第一页")
        w.write(0, 0, "id")
        w.write(0, 1, u"用户名")
        w.write(0, 2, u"密码")
        w.write(0, 3, u"手机号")
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            w.write(excel_row, 0, obj.id)
            w.write(excel_row, 1, obj.name)
            w.write(excel_row, 2, obj.password)
            w.write(excel_row, 3, obj.phone)
            excel_row += 1
        output = io.BytesIO()
        wb.save(output)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=user.xls'
        # 重新定位到开始
        output.seek(0)
        response.write(output.getvalue())
        return response


def importExcel(request):
    '''
    :param request:
    :return: 上传文件excel表格 ,并进行解析
    '''
    if request.method != "POST":
        return HttpResponse("不是post请求")
    f = request.FILES['file']
    type_excel = f.name.split('.')[1]
    if 'xlsx' != type_excel:
        return HttpResponse("上传文件格式不是xlsx")
    # 开始解析上传的excel表格
    wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
    table = wb.sheets()[0]
    nrows = table.nrows  # 行数
    # ncole = table.ncols  # 列数
    list = []
    for i in range(1, nrows):
        user = User();
        rowValues = table.row_values(i)  # 一行的数据
        user.name = rowValues[0]
        user.password = rowValues[1]
        user.phone = rowValues[2]
        list.append(user)

    User.objects.bulk_create(list)

    return HttpResponse("操作成功")
