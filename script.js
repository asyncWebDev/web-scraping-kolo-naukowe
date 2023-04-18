console.log("hello students");

const students = [
  { name: "Bartek", age: 30 },
  { name: "Krzyś", age: 23 },
  { name: "Aga", age: 24 },
];

const studentsList = document.querySelector("#students-list");

students.map((student, id) => {
  return studentsList.insertAdjacentHTML(
    "beforeend",
    `<p>Student number ${id + 1}, hello ${student.name}, you are ${
      student.age
    } years old</p>`
  );
});
