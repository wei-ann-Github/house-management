import argparse
import csv
import os
from pathlib import Path
from datetime import datetime
import sys

from . import db

EXPORT_PATH = Path('.planning/inventory_export.csv')


def cmd_init_db(args):
    db.init_db()
    print(f"Initialized DB at {db.DB_PATH}")


def cmd_add_item(args):
    item_id = db.insert_item(args.name, args.photo, args.dimensions, args.category, args.tag)
    print(f"Added item id={item_id} name={args.name}")


def cmd_add_cost(args):
    if args.quote and not Path(args.quote).exists():
        print(f"Warning: quote PDF path does not exist: {args.quote}")
    cost_id = db.insert_cost(args.description, args.amount, args.category, args.item_id, args.quote, args.paid)
    print(f"Added cost id={cost_id} amount={args.amount}")


def cmd_add_milestone(args):
    mid = db.insert_milestone(args.title, args.due)
    print(f"Added milestone id={mid} title='{args.title}' due={args.due}")


def cmd_export_inventory(args):
    EXPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(EXPORT_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name','photo_path','dimensions','category','tag','created_at'])
        for row in db.iter_items():
            writer.writerow([row['id'], row['name'], row['photo_path'] or '', row['dimensions'] or '', row['category'] or '', row['tag'] or '', row['created_at']])
    print(f"Exported inventory to {EXPORT_PATH}")


def cmd_list(args):
    if args.what == 'items':
        for r in db.iter_items():
            print(f"{r['id']}: {r['name']} ({r['category']}) tag={r['tag']}")
    elif args.what == 'costs':
        for r in db.list_costs():
            print(f"{r['id']}: {r['description']} ${r['amount']} item={r['item_id']} quote={r['quote_pdf_path']} paid={r['paid']}")
    elif args.what == 'milestones':
        for r in db.list_milestones():
            print(f"{r['id']}: {r['title']} due={r['due_date']} complete={r['complete']}")


def make_parser():
    p = argparse.ArgumentParser(prog='house-management')
    sub = p.add_subparsers(dest='cmd')

    sp = sub.add_parser('init-db')
    sp.set_defaults(func=cmd_init_db)

    sp = sub.add_parser('add-item')
    sp.add_argument('--name', required=True)
    sp.add_argument('--photo')
    sp.add_argument('--dimensions')
    sp.add_argument('--category')
    sp.add_argument('--tag')
    sp.set_defaults(func=cmd_add_item)

    sp = sub.add_parser('add-cost')
    sp.add_argument('--description', required=True)
    sp.add_argument('--amount', required=True, type=float)
    sp.add_argument('--category')
    sp.add_argument('--item-id', dest='item_id', type=int)
    sp.add_argument('--quote', help='Path to quote PDF')
    sp.add_argument('--paid', action='store_true')
    sp.set_defaults(func=cmd_add_cost)

    sp = sub.add_parser('add-milestone')
    sp.add_argument('--title', required=True)
    sp.add_argument('--due')
    sp.set_defaults(func=cmd_add_milestone)

    sp = sub.add_parser('export-inventory')
    sp.set_defaults(func=cmd_export_inventory)

    sp = sub.add_parser('list')
    sp.add_argument('what', choices=['items','costs','milestones'])
    sp.set_defaults(func=cmd_list)

    return p


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    p = make_parser()
    args = p.parse_args(argv)
    if not hasattr(args, 'func'):
        p.print_help()
        return 2
    return args.func(args)


if __name__ == '__main__':
    raise SystemExit(main())
