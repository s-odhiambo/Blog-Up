"""Initial Migration

Revision ID: cd0ab6ded55f
Revises: 
Create Date: 2019-12-02 09:00:18.574932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd0ab6ded55f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.Column('content', sa.String(length=300), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitches_content'), 'pitches', ['content'], unique=False)
    op.create_index(op.f('ix_pitches_title'), 'pitches', ['title'], unique=False)
    op.add_column('comments', sa.Column('date', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('post_comment', sa.String(length=255), nullable=True))
    op.add_column('comments', sa.Column('time', sa.String(), nullable=True))
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_index(op.f('ix_comments_post_comment'), 'comments', ['post_comment'], unique=False)
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'comment')
    op.drop_column('comments', 'post_id')
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'image_file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('image_file', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'bio')
    op.add_column('comments', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('comments', sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_index(op.f('ix_comments_post_comment'), table_name='comments')
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('comments', 'time')
    op.drop_column('comments', 'post_comment')
    op.drop_column('comments', 'pitch_id')
    op.drop_column('comments', 'date')
    op.drop_index(op.f('ix_pitches_title'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_content'), table_name='pitches')
    op.drop_table('pitches')
    # ### end Alembic commands ###
