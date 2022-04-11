# script to check if an entry in an xml file has duplicate id

def validate(xml_file):
    import xml.etree.ElementTree as ET
    tree = ET.parse(xml_file)
    root = tree.getroot()
    admin_ids = []
    member_ids = []
    for role_child in root:
        for user in role_child:
            print(user.tag, user.attrib)
            if user.tag == 'admin' or user.tag == 'member':
                user_id = user.find('id').text
                if user.tag == 'admin':
                    if user_id in admin_ids:
                        raise Exception('Duplicate admin id: {}'.format(user_id))
                    else:
                        admin_ids.append(user_id)
                elif user.tag == 'member':
                    if user_id in member_ids:
                        raise Exception('Duplicate member id: {}'.format(user_id))
                    else:
                        member_ids.append(user_id)


def main():
    import sys
    if len(sys.argv) != 2:
        print('Usage: validate.py <xml_file>')
        sys.exit(1)
    validate(sys.argv[1])


if __name__ == '__main__':
    main()
