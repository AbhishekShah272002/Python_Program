wt_limit = 30

def baggage_check(baggage_wt):
  extra_baggage_charge=0
  if not(baggage_wt>=0 and baggage_wt<=wt_limit):
    extra_baggage=baggage_wt-wt_limit
    extra_baggage_charge=extra_baggage*100
