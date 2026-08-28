import user_manager
import logging

logging.basicConfig(
    level = logging.DEBUG, 
    filename = 'test.log',
    filemode = 'w'
)

if __name__ == "__main__":
        Manager = user_manager.UserManager()

        logging.info('Test case 1(RF1)')
        Manager.add_user(1, "Alice")
        logging.info('PASS using the debugger')
        logging.info('Finalizó el test 1')



        logging.info('Test case 2(RF2)')
        Manager.add_user(2, "Bob")
        Manager.add_user(3, "Charlie")
        user1 = Manager.find_user(2)
        logging.info('Before if')
        if user1["name"] == 'Bob':
            logging.info('PASS')
        else:
              logging.info('FAIL')
        logging.info('Finalizó el test 2')



        logging.info('Test case 3(RF3)')
        Manager.delete_user(3)
        logging.info("Test passed using debugger")
        logging.info('Finalizó el test 3')



        logging.info('Test case 4(RF4)')
        all_names = Manager.get_all_names()
        logging.info(f'Los nombres son:{all_names}')
        if all_names == ['Alice', 'Bob']:
              logging.info('PASS')
        else:
              logging.error('FAIL')
              logging.warning('La funcion devuelve los ids')
        logging.info('Finalizó el test 4')


        logging.info('Test case 5(RFN1)')
        for i in range(1000):
              Manager.add_user(i,'user' +str(i))
        logging.info('Passed using debugger')
        logging.info('Finalizó el test 5')


