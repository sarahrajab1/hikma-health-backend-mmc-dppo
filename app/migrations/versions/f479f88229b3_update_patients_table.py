"""update patients table

Revision ID: f479f88229b3
Revises: e778cb1d223e
Create Date: 2022-11-08 13:24:09.330797

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'f479f88229b3'
down_revision = 'e778cb1d223e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE patients ADD COLUMN locality text')
    op.execute('ALTER TABLE patients ADD COLUMN city text')
    op.execute('ALTER TABLE patients ADD COLUMN hai_village text')
    op.execute('ALTER TABLE patients ADD COLUMN blok_no text')
    op.execute('ALTER TABLE patients ADD COLUMN house_no text')
    op.execute('ALTER TABLE patients ADD COLUMN occupation text')
    op.execute('ALTER TABLE patients ADD COLUMN insurance text')
    op.execute('ALTER TABLE patients ADD COLUMN private_insurance text')
    op.execute('ALTER TABLE patients ADD COLUMN id_number text')
    op.execute('ALTER TABLE patients ADD COLUMN record_number text')
    op.execute('ALTER TABLE patients ADD COLUMN clinic_estate text')
    op.execute('ALTER TABLE patients ADD COLUMN clinic_city text')
    op.execute('ALTER TABLE patients ADD COLUMN clinic_name text')
    op.execute('ALTER TABLE patients ADD COLUMN first_register_date DATE')


def downgrade():
    op.execute('ALTER TABLE patients DROP COLUMN locality')
    op.execute('ALTER TABLE patients DROP COLUMN city')
    op.execute('ALTER TABLE patients DROP COLUMN hai_village')
    op.execute('ALTER TABLE patients DROP COLUMN blok_no')
    op.execute('ALTER TABLE patients DROP COLUMN house_no')
    op.execute('ALTER TABLE patients DROP COLUMN occupation')
    op.execute('ALTER TABLE patients DROP COLUMN insurance')
    op.execute('ALTER TABLE patients DROP COLUMN private_insurance')
    op.execute('ALTER TABLE patients DROP COLUMN id_number')
    op.execute('ALTER TABLE patients DROP COLUMN record_number')
    op.execute('ALTER TABLE patients DROP COLUMN clinic_estate')
    op.execute('ALTER TABLE patients DROP COLUMN clinic_city')
    op.execute('ALTER TABLE patients DROP COLUMN clinic_name')
    op.execute('ALTER TABLE patients DROP COLUMN first_register_date')
