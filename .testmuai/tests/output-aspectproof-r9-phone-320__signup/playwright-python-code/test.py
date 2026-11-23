import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="075bc0ee-9500-4a72-8582-a796fb529f05",
    name="Web || laxmanbusetty || TC-95",
    tc_id="TC-95",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"you_re_subscribed_message_visible": "true", "issues_seen_this_session_zero": "true", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (89 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r9-phone-320__signup&start=%2F', instruction_id='d1283584-e5f9-4105-ab2c-be503b674972'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r9-phone-320__signup&start=%2F")
    
    async with testmu.step('Waiting while the form fields populate', instruction_id='cf80b87c-4414-4690-818e-a8363e7fc1b0'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='783a50d3-7df6-4995-a796-64fb07e41fcc'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='128ce8ed-b09e-452d-8c46-7996d079d897'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
    
    async with testmu.step('Waiting for the Get trail notes form to be ready', instruction_id='71197709-1515-45bf-8b31-adfad42f1e67'):
        await page.wait_for_timeout(200)
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button', instruction_id='5e3b56bf-a69d-4574-91a8-3ba3bdc18f05'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('you_re_subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='55d770ce-3db8-4b0f-aecb-dd0cc8a3a551'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{you_re_subscribed_message_visible}}', 'store_key': 'you_re_subscribed_message_visible', 'variable_refs': {'{{you_re_subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'you_re_subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{you_re_subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Waiting for the AspectProof layout panel to finish loading', instruction_id='5a38ff71-d3e7-4410-bd01-62c70bd12df1'):
        await page.wait_for_timeout(200)
    
    async with testmu.step('Checking whether the session issue count is present'):
        set_var('issues_seen_this_session_zero', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Issues seen this session:\\s*0\\b/.test(el(24).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the text "Issues seen this session: 0" is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Reading the AspectProof layout panel report'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text content of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='1ac913f5-c050-4852-81af-4335c8148d95'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'store_key': 'issues_seen_this_session_zero', 'variable_refs': {'{{issues_seen_this_session_zero}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session_zero', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'it shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)