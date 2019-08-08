from blog.models import User
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
import xlrd


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
        print(type(rowValues[0]))
        user.name = rowValues[0]
        user.password = rowValues[1]
        user.phone = rowValues[2]
        list.append(user)

    User.objects.bulk_create(list)

    return HttpResponse("操作成功")
