export default function getStudentIdsSum(students) {
    const addStudents = students.reduce(add = () => students.id++)
    return addStudents
}