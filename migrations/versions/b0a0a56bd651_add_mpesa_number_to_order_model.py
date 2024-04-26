"""Add mpesa_number to Order model

Revision ID: b0a0a56bd651
Revises: 25039174e7b9
Create Date: 2023-11-21 12:00:31.713050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0a0a56bd651'
down_revision = '25039174e7b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('mpesa_number',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.Float(),
               nullable='default_value')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('mpesa_number',
               existing_type=sa.Float(),
               type_=sa.VARCHAR(length=15),
               nullable=False)

    # ### end Alembic commands ###
