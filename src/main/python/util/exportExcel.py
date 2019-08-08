from xlwt import Workbook
import io
from blog.models import User
from django.shortcuts import HttpResponse  # 导入HttpResponse模块


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