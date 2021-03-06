"""change column name limit to signup_limit

Revision ID: c3fc3ce612aa
Revises: 4679a960c1ec
Create Date: 2018-09-13 01:38:34.797232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c3fc3ce612aa'
down_revision = '4679a960c1ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('competition', sa.Column('signup_limit', sa.Integer(), nullable=False))
    op.drop_column('competition', 'limit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('competition', sa.Column('limit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('competition', 'signup_limit')
    # ### end Alembic commands ###
