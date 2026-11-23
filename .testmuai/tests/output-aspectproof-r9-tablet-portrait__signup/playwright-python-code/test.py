import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="597f8ba1-766e-4941-ab88-bb39e6541959",
    name="Subscribe to Trail Notes and Verify Layout Panel",
    tc_id="TC-83",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"subscribed_message_visible": "true", "issues_seen_this_session_check": "true", "layout_report": "AspectProof layout\nTablet portrait 768\u00d71024 \u00b7 portrait\nProbe: active (90 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-portrait&run=r9-tablet-portrait__signup&start=%2F', instruction_id='c8002196-bddb-48c8-af9c-bdc12bd76e8f'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-portrait&run=r9-tablet-portrait__signup&start=%2F")
    
    async with testmu.step('Waiting for the plan to be ready for typing Name and Email', instruction_id='10630b97-395f-4acd-9170-081385be4be8'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='58e8a6d0-9394-4780-999a-8a64f149efd5'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='38da2e35-8318-46c3-bd3c-b9a9751996e2'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button', instruction_id='bbd1c2b0-e0bc-423b-905c-fcccffc4d440'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='73a00db5-7e21-4a76-b649-d3f4b9efce50'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'store_key': 'subscribed_message_visible', 'variable_refs': {'{{subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Reading the AspectProof layout panel', instruction_id='562be8fa-f91e-4a53-8baf-8316d569ff81'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Checking whether the issues-seen session count is present'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {30: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/^Issues seen this session:\\s*0\\s*$/.test(el(30).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='whether the "Issues seen this session: 0" text is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {27: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(27).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='add308ef-f1b0-4293-a71a-8c5539289fd4'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session_check', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)