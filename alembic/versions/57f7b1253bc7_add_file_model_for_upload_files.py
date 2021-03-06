"""add File model for upload files

Revision ID: 57f7b1253bc7
Revises: c3fc3ce612aa
Create Date: 2018-09-13 15:19:56.028930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57f7b1253bc7'
down_revision = 'c3fc3ce612aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('competition_news_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['competition_news_id'], ['competition_news.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###
