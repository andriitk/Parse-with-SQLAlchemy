"""Init

Revision ID: 30671560f067
Revises: 
Create Date: 2022-08-17 15:32:38.644793+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30671560f067'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=250), nullable=False),
    sa.Column('author_link', sa.String(length=150), nullable=False),
    sa.Column('created at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('keywords',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('keyword', sa.String(length=150), nullable=False),
    sa.Column('created at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('keyword')
    )
    op.create_table('quotes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=500), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('created at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('quote_keyword',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote', sa.Integer(), nullable=True),
    sa.Column('keyword', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['keyword'], ['keywords.id'], ),
    sa.ForeignKeyConstraint(['quote'], ['quotes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote_keyword')
    op.drop_table('quotes')
    op.drop_table('keywords')
    op.drop_table('authors')
    # ### end Alembic commands ###