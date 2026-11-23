import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="bba89112-62c2-47e9-9503-d575ca7a7627",
    name="Subscribe to Trail Notes and Verify Layout Panel",
    tc_id="TC-13",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"youre_subscribed_message_appears": "true", "aspectproof_issues_seen_this_session": "AspectProof layout\nTablet portrait 768\u00d71024 \u00b7 portrait\nProbe: active (78 scans)\nIssues now: 0\nIssues seen this session: 0", "layout_report": "AspectProof layout\nTablet portrait 768\u00d71024 \u00b7 portrait\nProbe: active (78 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-portrait&run=r3-tablet-portrait__signup&start=%2F', instruction_id='6ce0bc3b-7297-4add-a5fe-db540e47e7cc'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-portrait&run=r3-tablet-portrait__signup&start=%2F")
    
    async with testmu.step('Waiting while the form steps are queued', instruction_id='fe176302-ce2e-4ea1-9743-69c977452468'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='608f4a6e-ca3d-4192-a335-2090a9542a53'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='eef3783e-f13f-43bd-8a5f-3237674ba3e1'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button in the Get trail notes form', instruction_id='389f0f66-458a-49af-83fa-590fb0ad8e38'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('youre_subscribed_message_appears', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {19: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(19).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='3a4df0a6-bf06-4bb9-863f-7dfe7a5349d8'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{youre_subscribed_message_appears}}', 'store_key': 'youre_subscribed_message_appears', 'variable_refs': {'{{youre_subscribed_message_appears}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'youre_subscribed_message_appears', 'expected_value': 'true', 'extracted_value': '{{youre_subscribed_message_appears}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Reading the issues count from the AspectProof layout panel'):
        set_var('aspectproof_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the text displayed in the AspectProof layout panel', expected_value='Issues seen this session: 0', needs_unit_conversion=False, operator='contains', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='c883a31a-e5b0-44cd-8165-e5566e425faf'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'contains', 'transforms': [], 'json_path': None, 'expected': 'Issues seen this session: 0', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'store_key': 'aspectproof_issues_seen_this_session', 'variable_refs': {'{{aspectproof_issues_seen_this_session}}': 'AspectProof layout\nTablet portrait 768×1024 · portrait\nProbe: active (78 scans)\nIssues now: 0\nIssues seen this session: 0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_issues_seen_this_session', 'expected_value': 'Issues seen this session: 0', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'operator': 'contains', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)