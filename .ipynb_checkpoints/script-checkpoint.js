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
    `<p>Student number ${id + 1} ${Object.keys(student).map((key) => {
      return student[key];
    })}</p>`
  );
});
