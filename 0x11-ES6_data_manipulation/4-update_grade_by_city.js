export default function updateStudentGradeBycity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const updatedGrade = newGrades.find(
        (grade) => grade.studentId === student.id,
      );
      return {
        ...student,
        grade: updatedGrade ? updatedGrade.grade : 'N/A',
      };
    });
}
