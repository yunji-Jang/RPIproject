# smbus library
import smbus

# time library
import time
import I2C_driver as LCD


bus = smbus.SMBus(1)

# IC address
address = 0x53

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# ADXL345 init
def init_ADXL345():    
    bus.write_byte_data(address, 0x2D, 0x08)

# data measure
def measure_acc(adr):    
    acc0 = bus.read_byte_data(address, adr)

    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0

    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    acc = acc * 3.9 / 1000

    return acc


def main():
    init_ADXL345()
    mylcd = LCD.lcd()

    while 1:

        x = input()

        if x == ("1"):
            x_acc = measure_acc(x_adr)
            y_acc = measure_acc(y_adr)
            z_acc = measure_acc(z_adr)

            print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')

            mylcd.lcd_clear()

        elif x == ("2"):

            mylcd.lcd_display_string("Hello World",1)
            mylcd.lcd_display_string("Raspberry pi3 b+",2)
           
            time.sleep(5)

            mylcd.lcd_clear()
            mylcd.lcd_display_string("LCD display",2)

        else:
            mylcd.lcd_display_string("Quit",1)
            time.sleep(1)
            mylcd.lcd_clear()


        
if __name__ == '__main__':
    main()



