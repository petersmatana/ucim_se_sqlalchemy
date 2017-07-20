"""empty message

Revision ID: d2f222aafa4e
Revises: 
Create Date: 2017-07-21 01:24:20.063315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2f222aafa4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('restaurant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], [u'restaurants.id'], name=u'menu_items_restaurant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'menu_items_pkey')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'restaurants_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###