#!/usr/bin/node
const callMeMoby = (x, theFunction) => {
  if (x <= 0) {
    return;
  }

  theFunction();
  callMeMoby(x - 1, theFunction);
};

module.exports = {
  callMeMoby
};
