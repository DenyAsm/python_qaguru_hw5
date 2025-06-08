from selene import browser, be, have



def test_add_data_registration_and_submit(demo_qa):
    browser.element('.practice-form-wrapper').should(be.visible and have.text('Practice Form'))
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name')).type('Petr')
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name')).type('Petrov')
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com')).type('NAME@gmail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number')).type('0123456789')
    browser.element('#dateOfBirthInput').should(have.attribute('placeholder')).click()
    browser.element('.react-datepicker__month-select').should(be.visible).click()
    browser.element('[value="4"]').click()
    browser.element('.react-datepicker__year-select').should(be.visible).click()
    browser.element('[value="2000"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#dateOfBirthInput').should(have.value('20 May 2000'))
    browser.element('#subjectsInput').type('Maths').type('Physics').press_enter()

    breakpoint()

