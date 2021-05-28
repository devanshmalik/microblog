"""add followers

Revision ID: 43b11a80cb68
Revises: 70cad7056fac
Create Date: 2021-05-27 19:03:38.848603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43b11a80cb68'
down_revision = '70cad7056fac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
