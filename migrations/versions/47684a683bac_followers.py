"""followers

Revision ID: 47684a683bac
Revises: 9cf08515c46d
Create Date: 2020-03-03 21:20:39.952384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47684a683bac'
down_revision = '9cf08515c46d'
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
