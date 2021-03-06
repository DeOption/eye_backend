"""empty message

Revision ID: 276216d4cae5
Revises: 31c1cbe832fd
Create Date: 2021-06-02 19:57:24.588703

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '276216d4cae5'
down_revision = '31c1cbe832fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leave_hospital_slj',
    sa.Column('leave_hospital_slj_id', sa.VARCHAR(length=20), nullable=False, comment='三棱镜(出院)表id'),
    sa.Column('base_info_id', sa.VARCHAR(length=20), nullable=True, comment='基本表id'),
    sa.Column('leave_hospital_slj_near', sa.VARCHAR(length=10), nullable=True, comment='视近'),
    sa.Column('leave_hospital_slj_far', sa.VARCHAR(length=20), nullable=True, comment='视远'),
    sa.ForeignKeyConstraint(['base_info_id'], ['base_info.id'], ),
    sa.PrimaryKeyConstraint('leave_hospital_slj_id')
    )
    op.drop_table('leave_hospital_slj_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leave_hospital_slj_id',
    sa.Column('leave_hospital_slj_id', mysql.VARCHAR(length=20), nullable=False, comment='三棱镜(出院)表id'),
    sa.Column('base_info_id', mysql.VARCHAR(length=20), nullable=True, comment='基本表id'),
    sa.Column('leave_hospital_slj_near', mysql.VARCHAR(length=10), nullable=True, comment='视近'),
    sa.Column('leave_hospital_slj_far', mysql.VARCHAR(length=20), nullable=True, comment='视远'),
    sa.ForeignKeyConstraint(['base_info_id'], ['base_info.id'], name='leave_hospital_slj_id_ibfk_1'),
    sa.PrimaryKeyConstraint('leave_hospital_slj_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('leave_hospital_slj')
    # ### end Alembic commands ###
