export default function getListStudentIds(arr) {
  if (!Array.isArray(arr)) {
    const emptyArray = [];
    return emptyArray;
  }
  const studentsArr = arr.map((item) => item.id);
  return studentsArr;
}
