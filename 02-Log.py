import logging
import sys

main = logging.getLogger('main')
main.setLevel(logging.DEBUG)

handler = logging.FileHandler('app.log')

format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(format)

main.addHandler(handler)

main.info('This is an information about something.')
main.error('We cant divide any numbers by zero.')
# main.notice('Someone loves your status.')
main.warning('Insufficient funds.')
main.debug('This is debug message.')
# main.alert('Achtung! Achtung!')
main.critical('Medic!! Weve got critical damages.')
# main.emergency('System hung. Contact system administrator immediately!')
