#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 Mikhail Kondrashin
# michael_kondrashin@trendmicro.com
#

import sys, string, hashlib

USAGE = """Usage:\n {} file template target
    file - text file with six digit card number prefixes
    template - data identifier template file (XML)
    target - target file name
""".format(sys.argv[0])

NO_ONE_NUMBER = True

def generate_id(salt):
    hash = hashlib.sha1()
    hash.update(salt)
    h = hash.hexdigest()
    return  "%s-%s-%s-%s-%s" % (h[0:8], h[8:12], h[12:16], h[16:20], h[20:32])


def generate_rule(prefix):
    JUST_FOR_RULE___RULE_TEMPLATE="""
                        <buildingBlock entityHits="1" operation="OR" sourceName="${name}" sourceType="ENTITY"/>"""

    RULE_TEMPLATE="""
                    <matchRule operation="OR">
                        <buildingBlock entityHits="1" sourceName="${name}" sourceType="ENTITY"/>
                    </matchRule>"""

    rule_template = string.Template(RULE_TEMPLATE)
    name = generate_id(prefix)
    return rule_template.substitute(name=name)


def generate_asset(prefix, number):

    DISPLAY_TEMPLATE = 'Raiffeisen Credit Card ${number}'
    display_template = string.Template(DISPLAY_TEMPLATE)
    display = display_template.substitute(number="%03d" % number)

    DESCRIPTION_TEMPLATE = 'Raiffeisen Credit Card with prefix ${prefix}'
    description_template = string.Template(DESCRIPTION_TEMPLATE)
    description = description_template.substitute(prefix=prefix)

    REGEX_TEMPLATE = '[^\d-](${ABCD}${EF}\d{8,10}|${ABCD}[-. ]${EF}\d{2}[-. ]\d{4}[-. ]\d{4}|${ABCD}[-. ]${EF}\d{4}[-. ]\d{5})[^\d-]'
    if NO_ONE_NUMBER:
        REGEX_TEMPLATE = '[^\d-](${ABCD}[-. ]${EF}\d{2}[-. ]\d{4}[-. ]\d{4}|${ABCD}[-. ]${EF}\d{4}[-. ]\d{5})[^\d-]'
    regex_template = string.Template(REGEX_TEMPLATE)
    regex = regex_template.substitute(ABCD=prefix[0:4], EF=prefix[4:6])

    PATTERN_TEMPLATE = "${ABCD}-${EF}nn-nnnn-nnnn OR ${ABCD}${EF}nnnnnnnnnn OR ${ABCD}${EF}nnnnnnnnn OR ${ABCD}-${EF}nnnn-nnnnn, etc."
    if NO_ONE_NUMBER:
        PATTERN_TEMPLATE = "${ABCD}-${EF}nn-nnnn-nnnn OR ${ABCD}-${EF}nnnn-nnnnn, etc."
    pattern_template = string.Template(PATTERN_TEMPLATE)
    pattern = pattern_template.substitute(ABCD=prefix[0:4], EF=prefix[4:6])

    ASSET_TEMPLATE = """
                <entity caseSensitive="false" description="${description}" display_name="${display}" maxLength="19" minLength="14" name="${name}" pre-defined="false" type="Type 1" validator="CreditCardNumber">
                    <alphabetCharset><![CDATA[0123456789-.]]></alphabetCharset>
                    <regularExpression><![CDATA[${regex}]]></regularExpression>
                    <patternForDisplay><![CDATA[${pattern}]]></patternForDisplay><examples/>
                </entity>"""
    asset_template = string.Template(ASSET_TEMPLATE)
    asset = asset_template.substitute(
            description = description,
            display = display,
            name = generate_id(prefix),
            regex = regex,
            pattern = pattern
        )
    return asset


def iterate_prefixes(iin):
    for prefix in iin.splitlines():
        if len(prefix) != 6:
            print('Skip {} - lenght is not 6'.format(prefix))
            continue
        if not prefix.isdigit():
            print('Skip {} - not only digits'.format(prefix))
            continue
        yield prefix


def generate_template(iin, template):
    rules = []
    assets = []
    for N, prefix in enumerate(iterate_prefixes(iin)):
        rules.append(generate_rule(prefix))
        assets.append(generate_asset(prefix, N))

    print("Processed {} prefixes".format(N+1))

    #template_text = open(template_name,'r').read()
    compliance_template = string.Template(template)
    rules_text = "".join(rules)
    assets_text = "".join(assets)
    compliance = compliance_template.substitute(
        rules = rules_text,
        assets = assets_text
        )

    return compliance


def generate_template_from_files(iin_file_name, template_file_name):
    return generate_template(open(iin_file_name, 'r').read(), open(template_file_name,'r').read())


def process(iin_name, template_name, target_name):
    compliance = generate_template_from_files(iin_name, template_name)
    open(target_name, 'w').write(compliance)
    print("Result saved to {}".format(target_name))


def main():
    if len(sys.argv) != 4:
        print(USAGE)
        return 1
    process(sys.argv[1], sys.argv[2], sys.argv[3])
    return 0


if __name__ == '__main__':
    sys.exit(main())
