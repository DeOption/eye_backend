from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.leave_hospital_tsj import LeaveHospitalTsj
from app.snow.snowflake import worker
from typing import Any

class CRUDLeaveHospitalTsj(CRUDBase[None, LeaveHospitalTsj, None]):
    def createLeaveHospitalTsj(
            self,
            db: Session,
            base_info_id: str,
            data: dict
    ) -> Any:
        """
        添加出院同视机
        :param db: 数据库连接对象
        :param base_info_id: 病例ID
        :param data: {leave_tsj_tss, leave_tsj_tss_sp, leave_tsj_tss_cz, leave_tsj_tss_cs_z}
        :return: None
        """
        leave_tsj_id = worker.get_id()
        data = jsonable_encoder(data)
        db_obj = LeaveHospitalTsj(
            base_info_id = base_info_id,
            leave_tsj_id = leave_tsj_id,
            **data
        )

        return db_obj

    def updateLeaveHospitalTsj(self, db: Session, id: str, data: dict) -> Any:
        """修改出院同视机"""
        data = jsonable_encoder(data)
        db.query(LeaveHospitalTsj).filter(LeaveHospitalTsj.base_info_id == id).update(data)

        return None


leavehospitalslj = CRUDLeaveHospitalTsj(LeaveHospitalTsj)
