export default function getStudentIdsSum(students) {
  const sumIds = students.reduce((accumulator, currentStudent) => accumulator + currentStudent.id, 0);

  return sumIds;
}
