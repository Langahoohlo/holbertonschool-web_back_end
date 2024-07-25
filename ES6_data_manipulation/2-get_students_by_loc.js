function getStudentsByLocation(students, city) {
    const studentsByLocation = students.filter(students => students.location === city)
    return studentsByLocation
}

export default getStudentsByLocation