"""roles table

Revision ID: ae0452037c7b
Revises: bbdbfb891ef7
Create Date: 2019-03-25 15:19:39.148267

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = 'ae0452037c7b'
down_revision = 'bbdbfb891ef7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', sa.Text(), nullable=True))
    op.drop_column('user', 'addres')
    op.drop_constraint('user_roles_roles_fk_fkey', 'user_roles', type_='foreignkey')
    op.drop_constraint('user_roles_users_fk_fkey', 'user_roles', type_='foreignkey')
    op.create_foreign_key(None, 'user_roles', 'role', ['role_id'], ['id'])
    op.create_foreign_key(None, 'user_roles', 'user', ['user_id'], ['id'])
    op.drop_column('user_roles', 'roles_fk')
    op.drop_column('user_roles', 'users_fk')
    # ### end Alembic commands ###
    
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_roles', sa.Column('users_fk', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user_roles', sa.Column('roles_fk', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_roles', type_='foreignkey')
    op.drop_constraint(None, 'user_roles', type_='foreignkey')
    op.create_foreign_key('user_roles_users_fk_fkey', 'user_roles', 'user', ['users_fk'], ['id'])
    op.create_foreign_key('user_roles_roles_fk_fkey', 'user_roles', 'role', ['roles_fk'], ['id'])
    op.add_column('user', sa.Column('addres', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('user', 'address')
    # ### end Alembic commands ###
