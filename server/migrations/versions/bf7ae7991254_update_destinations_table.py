"""Update destinations table

Revision ID: bf7ae7991254
Revises: 
Create Date: 2025-01-27 17:16:22.857464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf7ae7991254'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('destinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.Column('safety_rating', sa.Integer(), nullable=False),
    sa.Column('activities', sa.String(length=500), nullable=False),
    sa.Column('image', sa.String(length=500), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('destinations')
    # ### end Alembic commands ###
