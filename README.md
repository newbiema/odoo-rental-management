# Odoo Rental Management

Project ini saya buat untuk belajar dasar-dasar **Odoo Development** menggunakan Odoo 19.

Tujuan utama project ini bukan untuk production, tapi untuk memahami bagaimana cara membuat custom module di Odoo dari awal.

## Yang Saya Pelajari

Dari project ini, saya belajar beberapa konsep dasar Odoo:

- Struktur custom module
- `__manifest__.py`
- Model di Odoo
- Odoo ORM
- Field seperti:
  - `Char`
  - `Date`
  - `Integer`
  - `Float`
  - `Selection`
  - `Many2one`
- Relasi dengan model bawaan Odoo `res.partner`
- Membuat List View
- Membuat Form View
- Membuat Menu dan Action
- Access Rights dengan `ir.model.access.csv`
- Upgrade custom module
- Koneksi Odoo dengan PostgreSQL

## Fitur Saat Ini

Module ini masih sederhana dan memiliki fitur:

- Menambahkan Rental Order
- Memilih Customer dari Contacts Odoo
- Menyimpan tanggal rental
- Menyimpan durasi rental
- Menyimpan harga
- Menyimpan status rental:
  - Draft
  - Ongoing
  - Done

## Struktur Module

```text
rental_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── rental.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── rental_views.xml
