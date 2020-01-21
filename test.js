

var fs = require('fs')

fs.readFile('./jsonFile.json', 'utf-8', function(err, data){
  if(err) throw err
  var arrayOfObjects = JSON.parse(data);
  arrayOfObjects.users.push({
    name: "Dani",
    age: 21
  })

  console.log(arrayOfObjects);


  fs.writeFile('./jsonFile.json', JSON.stringify(arrayOfObjects), 'utf-8', function(err){
    if(err) throw err
    console.log('Done!');
  })

})