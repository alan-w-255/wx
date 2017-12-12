import os
cur_dir = os.path.abspath(os.curdir)
# [app]
root_path=cur_dir

# [menu]
menu=os.path.join(cur_dir, 'account/menu.json')

# [debug]
debug_mode=True

# [account]
appID='wx2b673dde262bf217'
appsecret='2127f95bd32da08973cf2be5d151cb7d'

# [static]
# static_url='http://220.167.38.97/static'

# [webpage]
# user_binding_page='http://heywym.com/user_binding'

# [semester]
semester = '2017-下'

# [db]
DATABASE_URI = "sqlite:////app/data.sqlite"

# [date]
school_open_day = [2017,9,3]
