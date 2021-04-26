# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

#---------------------------------------------------------------------------------------------
# Declare import modules
#---------------------------------------------------------------------------------------------

import report
from datetime import date, timedelta, datetime
#, sys, pathlib
from arguments import get_arguments
from csv_buy import buy
from csv_sell import sell
from utils import get_current_date, advance_date, set_date

# Your code below this line.


#---------------------------------------------------------------------------------------------
# Main routine
#---------------------------------------------------------------------------------------------

def main():
    
    # Read config file for date
    current_date = get_current_date()
    
    # Get command line arguments
    args = get_arguments()
    
    # Check date handling commands and execute the corresponding routine
    if args.advance_date != None:
        current_date = advance_date(args.advance_date)
        return current_date
    if args.set_date != None:
        current_date = set_date(args.set_date)
        return current_date
    
    # Check commands and execute the corresponding routine
    if args.CLI_command.lower() == 'buy': print(buy(args.product_name, args.buy_date, args.price, args.expiration_date))
    elif args.CLI_command.lower() == 'sell': print(sell(args.product_name, args.sell_date, args.price))
    elif args.CLI_command.lower() == 'report': 

        # Convert yesterday, now, today or date to date
        report_date = None
        if args.yesterday != None: 
            report_date = (datetime.strptime(current_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
        if args.now != None: 
            report_date = current_date
        if args.today != None: 
            report_date = current_date
        if args.date != None:
            report_date = args.date
        if report_date != None:
            print(report.show_report(args.report_name, report_date))
        else:
            print(f"ERROR: missing <date>")

    # Unknown command
    else:
        print(f"ERROR: unknown command '{args.CLI_command}' <buy, sell, report>")
    return

if __name__ == '__main__':
    main()