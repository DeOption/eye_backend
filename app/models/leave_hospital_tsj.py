from sqlalchemy import Column, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 同视机(出院)
class LeaveHospitalTsj(Base):
    __tablename__ = 'leave_hospital_tsj'

    leave_tsj_id = Column(VARCHAR(20), primary_key=True, comment="同视机(出院)表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    leave_tsj_tss = Column(Boolean, comment="同时视(出院)")
    leave_tsj_tss_sp = Column(VARCHAR(20), comment="同时视水平值(出院)")
    leave_tsj_tss_cz = Column(VARCHAR(20), comment="同时视垂直值（R/L or L/R）(出院)")
    leave_tsj_tss_cs_z = Column(VARCHAR(20), comment="同时视垂直值具体数值(出院)")

    baseInfo = relationship("BaseInfo", back_populates='leaveHospitalTsj')
