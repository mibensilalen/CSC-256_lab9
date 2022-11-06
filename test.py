import ddg

presidents = ['Biden', 'Trump', 'Washington','Jackson', 'Johnson', 'Obama', 'Harrison',
              'Clinton', 'Coolidge', 'Arthur', 'Eisenhower',
              'Roosevelt', 'Pierce', 'Bush','Lincoln', 'Ford',
              'Cleveland', 'Truman', 'Hoover', 'Taft', 'Buchanan',
              'Garfield', 'Polk', 'Madison', 'Monroe', 'Carter', 'Adams',
              'Kennedy', 'Tyler', 'Buren', 'Fillmore', 'Nixon', 'Reagan',
              'Hayes', 'Roosevelt', 'Jefferson', 'Grant', 'Harding',
              'Harrison', 'McKinley', 'Wilson', 'Taylor', ]

def test_ddg():
    list = []
    for x in ddg.json_data:
        list.append(x['Text'].split('-')[0].split()[-1])
    for k in presidents:
        assert k in list