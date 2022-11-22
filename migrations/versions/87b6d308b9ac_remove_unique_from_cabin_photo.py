"""Remove unique from cabin photo

Revision ID: 87b6d308b9ac
Revises: 
Create Date: 2022-11-21 22:20:01.337017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87b6d308b9ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cabin', schema=None) as batch_op:
        batch_op.drop_constraint('cabin_photo_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cabin', schema=None) as batch_op:
        batch_op.create_unique_constraint('cabin_photo_key', ['photo'])

    # ### end Alembic commands ###