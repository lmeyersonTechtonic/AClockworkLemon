describe('clocking in ', () => {

  it('Should visit login page', () => {
    cy.visit('https://300026.namelytcp.com/app/webclock/index.html#/EmployeeLogOn')
      .then(() => {
        cy.get('input.CustomControlNumeric').type(`${Cypress.env('timeClockId')}`).then(() => {
          cy.get('input.DefaultSubmitBehavior').click().then(() => {
            cy.wait(3000).then(() => {
              cy.get('li#ClockIn') ///.click().then(() => {
                // cy.get('input.DefaultSubmitBehavior') // .click();

                // .should(el => {
                //   expect(el).to.have.value('Continue').
                // })
              // })
                .should(el => {
                expect(el).to.contain.text('Clock In');
              });
            });
          });
        });
      });
    });
    
});
