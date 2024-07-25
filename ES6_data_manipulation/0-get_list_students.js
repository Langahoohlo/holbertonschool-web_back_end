export default function getListStudents() {
  const students1 = {
    id: 1,
    firstName: "Guillaume",
    location: "San Francisco",
  };
  const students2 = {
    id: 2,
    firstName: "James",
    location: "San Columbia",
  };
  const students3 = {
    id: 5,
    firstName: "Serena",
    location: "San Francisco",
  };

  const classRoom = [];

  classRoom.push(students1, students2, students3);

  return classRoom
}
