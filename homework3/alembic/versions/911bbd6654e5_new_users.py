"""New users

Revision ID: 911bbd6654e5
Revises: 03fd6e217ee6
Create Date: 2021-03-05 16:07:08.808107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '911bbd6654e5'
down_revision = '03fd6e217ee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    op.drop_table('address')
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_postId_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    op.drop_column('comments', 'postId')
    op.add_column('photos', sa.Column('album_id', sa.Integer(), nullable=True))
    op.drop_constraint('photos_albumid_fkey', 'photos', type_='foreignkey')
    op.create_foreign_key(None, 'photos', 'albums', ['album_id'], ['id'])
    op.drop_column('photos', 'albumid')
    op.add_column('users', sa.Column('city', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('company_bs', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('company_catchPhrase', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('company_name', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('geo_lat', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('geo_lng', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('street', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('suite', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('zipcode', sa.String(length=32), nullable=True))
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('users', 'zipcode')
    op.drop_column('users', 'suite')
    op.drop_column('users', 'street')
    op.drop_column('users', 'geo_lng')
    op.drop_column('users', 'geo_lat')
    op.drop_column('users', 'company_name')
    op.drop_column('users', 'company_catchPhrase')
    op.drop_column('users', 'company_bs')
    op.drop_column('users', 'city')
    op.add_column('photos', sa.Column('albumid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'photos', type_='foreignkey')
    op.create_foreign_key('photos_albumid_fkey', 'photos', 'albums', ['albumid'], ['id'])
    op.drop_column('photos', 'album_id')
    op.add_column('comments', sa.Column('postId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_postId_fkey', 'comments', 'posts', ['postId'], ['id'])
    op.drop_column('comments', 'post_id')
    op.create_table('address',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('street', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('suite', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('zipcode', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('geo_lat', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('geo_lng', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='address_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='address_pkey')
    )
    op.create_table('company',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('catchPhrase', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('bs', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='company_pkey')
    )
    # ### end Alembic commands ###
