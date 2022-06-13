# Credit Card Generator

This program can be used to generate DLP templates for Trend Micro
Products


## WORK FLOW

1. Prepare Template file (see section "CREATE TEMPLATE") or use
   SMID_Template.xml
2. Prepare IIN prefixes file (See section "PREFIXES FILE") or
   use IIN_Raiffeisen.txt
3. Use command line or gui tool to generate final
   Template. Both can be run from source in src directory
4. Upload final template to Trend Micro product
5. Create DLP policy to engage new template

**Note**: Launch command line tool to see usage description

**Note**: Launch gui tool and press Help button to see usage
   Description

## CREATE TEMPLATE

**Note**: Basic template is included: SMID_Template.xml. It will create new
      Template because it has its own unique ID

1. Open your Trend Micro product console
2. Navigate to DLP settings and create new Template with any Data Identifiers
3. Export this template

Then edit template using any text editor:
1. Between <complianceTemplates> and </complianceTemplates> remove all
   <template ...> </template> beside your template
2. Inside <template...> replace everything between <matchRule> and
   </matchRule> with ${rules}
2. Replace everything between <digitalAssets> and </digitalAssets>
   with ${assets}
3. Pay attention to following properties: version, description,
   display_name
4. Keep name property untouched, so during import template will
   Be replaced and not added as new one

## PREFIXES FILE

Prefixes file is text file with six digit prefixes in each line:
```
123456
654321
```
and so on

Wrong format lines will be ignored


## FILES

- IIN_Raiffeisen.txt - IIN file example
- SMID_Template.xml - template for Trend Micro products
- README.txt - this file
- Result_Template.xml - example of generated result for IIN
  File example and provided template
- ccard - Mac OS X command line tool to generate template
- ccard.exe - Windows command line tool to generate template
- gui_ccard - Mac OS X gui tool to generate template
- src/ccardprefix.py - command line tool source code
- src/gui.py - cross platform gui tool source code
- src/pyinst.sh - ccard and gui_ccard generator for Mac OS X
- src/pyinst.cmd - ccard and gui_ccard generator for Windows
