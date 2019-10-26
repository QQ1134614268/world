import os

from db.db import db
from global_variable import LOG_PATH, UPLOAD_FILE_PATH
from vo.OrganizationVO import OrganizationVO


def init_all():
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
    if not os.path.exists(UPLOAD_FILE_PATH):
        os.mkdir(UPLOAD_FILE_PATH)


def init_db():
    if not OrganizationVO.query.filter_by(id=1).first():
        vo = OrganizationVO(id=1, code="origin", parent_id=0, name="W&G company", level=0, full_name="/W&G company/",
                            full_path_code="/origin/", full_path_id="/1/")
        db.session.add(vo)
        db.session.commit()
