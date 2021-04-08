from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from app.sqlDB.base_class import Base

# 手术设计
class Surgery(Base):
    __tablename__ = 'surgery'

    surgery_id = Column(VARCHAR(20), primary_key=True, comment="手术设计表id")
    base_info_id = Column(VARCHAR(20), ForeignKey('base_info.id'), comment="基本表id")
    surgery_yb = Column(VARCHAR(10), comment="手术设计眼别")
    # muscle = Column(VARCHAR(50), comment="肌肉")
    # way = Column(VARCHAR(50), comment="方式")
    # value = Column(VARCHAR(50), comment="量值")
    # beizhu = Column(VARCHAR(50), comment="备注")

    external_rectus_way = Column(VARCHAR(20), comment="外直肌方式")
    external_rectus_value = Column(VARCHAR(20), comment="外直肌量值")
    internal_rectus_way = Column(VARCHAR(20), comment="内直肌方式")
    internal_rectus_value = Column(VARCHAR(20), comment="内直肌量值")
    upper_rectus_way = Column(VARCHAR(20), comment="上直肌方式")
    upper_rectus_value = Column(VARCHAR(20), comment="上直肌量值")
    lower_rectus_way = Column(VARCHAR(20), comment="下直肌方式")
    lower_rectus_value = Column(VARCHAR(20), comment="下直肌量值")
    upper_oblique_way = Column(VARCHAR(20), comment="上斜肌方式")
    upper_oblique_value = Column(VARCHAR(20), comment="上斜肌量值")
    lower_oblique_way = Column(VARCHAR(20), comment="下斜肌方式")
    lower_oblique_value = Column(VARCHAR(20), comment="下斜肌量值")
    beizhu = Column(VARCHAR(20), comment="备注")

    baseInfo = relationship("BaseInfo", back_populates='surgery1')
