from flaskblog import create_app,db

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flaskblog.models import *


app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User= User)

if __name__ == '__main__':
    manager.run()