import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4947cd04-b53a-41ea-a876-5af20668e368",
    name="Subscribe to Trail Notes and Verify Layout Panel",
    tc_id="TC-25",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"subscribed_message_visible": "true", "aspectproof_issues_session_check": "true", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (62 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r3-phone-320__signup&start=%2F', instruction_id='4d761e5c-bd1d-4b55-90aa-d2cdbb0a5fa1'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r3-phone-320__signup&start=%2F")
    
    async with testmu.step('Waiting for the queued plan steps to complete', instruction_id='85c3a203-f79a-4113-aad9-1dc20868718d'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='a6e2526f-ad15-425d-ae36-a086d4b919f4'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='f6fbc43a-171e-4970-a824-735f033b96b6'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
    
    async with testmu.step('Confirming the filled Get trail notes form', instruction_id='6f81d666-d913-46aa-bf30-246499dbaa34'):
        await page.wait_for_timeout(100)
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button for the trail notes form', instruction_id='dd29be10-a801-411a-91e7-42a0e1e2030a'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Checking whether the session issue count is present in the layout panel'):
        set_var('aspectproof_issues_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Issues seen this session:\\s*0/.test(el(24).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether "Issues seen this session: 0" is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='6698e49b-6e06-4bda-a838-a79d3a601f76'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'store_key': 'subscribed_message_visible', 'variable_refs': {'{{subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Assertion check', instruction_id='96e39486-1985-44f9-9284-a82e163da68d'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_session_check}}', 'store_key': 'aspectproof_issues_session_check', 'variable_refs': {'{{aspectproof_issues_session_check}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_issues_session_check', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)