"""empty message

Revision ID: 64bd8ac9b82f
Revises: 264f3e27f92b
Create Date: 2019-06-03 14:03:29.897387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64bd8ac9b82f'
down_revision = '264f3e27f92b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('creationDate', sa.DateTime(timezone=4), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'creationDate')
    # ### end Alembic commands ###
