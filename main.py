import argparse

from zeep import Client

SERVICE_WSDL = 'http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl'


def check_vat(vat):
    client = Client(SERVICE_WSDL)
    contry_code = vat[:2]
    vat_id = vat[2:]
    return bool(client.service.checkVat(contry_code, vat_id)['valid'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('VAT', help='VAT identification number')
    args = parser.parse_args()

    if check_vat(args.VAT):
        print('Valid')
    else:
        print('Invalid')
