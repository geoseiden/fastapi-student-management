var app = angular.module('myApp', []);

app.controller('MentorsController', function ($scope, $http) {
    $scope.mentors = [];  // Array to store mentors
    $scope.newMentor = {}; // Object to store the new mentor data
    $scope.selectedMentor = null;

    $scope.openAddMentorPopup = function () {
        document.getElementById('addMentorModal').style.display = 'block';
    };

    $scope.closeAddMentorPopup = function () {
        document.getElementById('addMentorModal').style.display = 'none';
    };

    $scope.addMentor = function () {
        $http.post('http://127.0.0.1:8000/mentors', $scope.newMentor)
            .then(function (response) {
                $scope.mentors.push(response.data);
                $scope.newMentor = {};
                $scope.closeAddMentorPopup();
            })
            .catch(function (error) {
                console.error("Error adding mentor: " + error);
            });
    };

    $scope.editMentor = function (mentor) {
        $scope.selectedMentor = angular.copy(mentor);
        document.getElementById('editMentorModal').style.display = 'block';
    };

    $scope.updateMentor = function () {
        $http.put('http://127.0.0.1:8000/mentors/' + $scope.selectedMentor.empid, $scope.selectedMentor)
            .then(function (response) {
                var index = $scope.mentors.findIndex(function (mentor) {
                    return mentor.empid === response.data.empid;
                });
                if (index !== -1) {
                    $scope.mentors[index] = response.data;
                }
                $scope.closeEditMentorPopup();
            })
            .catch(function (error) {
                console.error("Error updating mentor: " + error);
            });
    };

    $scope.closeEditMentorPopup = function () {
        $scope.selectedMentor = null;
        document.getElementById('editMentorModal').style.display = 'none';
    };

    $scope.deleteMentor = function (mentor) {
        var confirmation = confirm("Are you sure you want to delete this mentor?");
        if (confirmation) {
            $http.delete('http://127.0.0.1:8000/mentors/' + mentor.empid)
                .then(function () {
                    var index = $scope.mentors.indexOf(mentor);
                    if (index !== -1) {
                        $scope.mentors.splice(index, 1);
                    }
                })
                .catch(function (error) {
                    console.error("Error deleting mentor: " + error);
                });
        }
    };

    $scope.init = function () {
        $http.get('http://127.0.0.1:8000/mentors')
            .then(function (response) {
                $scope.mentors = response.data;
            })
            .catch(function (error) {
                console.error("Error fetching mentors: " + error);
            });
    };

    $scope.init();
});

app.controller('StudentsController', function ($scope, $http) {
    $scope.students = [];  // Array to store students
    $scope.newStudent = {}; // Object to store the new student data
    $scope.selectedStudent = null;

    $scope.openAddStudentPopup = function () {
        document.getElementById('addStudentModal').style.display = 'block';
    };

    $scope.closeAddStudentPopup = function () {
        document.getElementById('addStudentModal').style.display='none';
    };

    $scope.addStudent = function () {
        $http.post('http://127.0.0.1:8000/students', $scope.newStudent)
            .then(function (response) {
                $scope.students.push(response.data);
                $scope.newStudent = {};
                $scope.closeAddStudentPopup();
            })
            .catch(function (error) {
                console.error("Error adding student: " + error);
            });
    };

    $scope.editStudent = function (student) {
        $scope.selectedStudent = angular.copy(student);
        document.getElementById('editStudentModal').style.display = 'block';
    };

    $scope.updateStudent = function () {
        $http.put('http://127.0.0.1:8000/students/' + $scope.selectedStudent.regno, $scope.selectedStudent)
            .then(function (response) {
                var index = $scope.students.findIndex(function (student) {
                    return student.regno === response.data.regno;
                });
                if (index !== -1) {
                    $scope.students[index] = response.data;
                }
                $scope.closeEditStudentPopup();
            })
            .catch(function (error) {
                console.error("Error updating student: " + error);
            });
    };

    $scope.closeEditStudentPopup = function () {
        $scope.selectedStudent = null;
        document.getElementById('editStudentModal').style.display = 'none';
    };

    $scope.deleteStudent = function (student) {
        var confirmation = confirm("Are you sure you want to delete this student?");
        if (confirmation) {
            $http.delete('http://127.0.0.1:8000/students/' + student.regno)
                .then(function () {
                    var index = $scope.students.indexOf(student);
                    if (index !== -1) {
                        $scope.students.splice(index, 1);
                    }
                })
                .catch(function (error) {
                    console.error("Error deleting student: " + error);
                });
        }
    };

    $scope.init = function () {
        $http.get('http://127.0.0.1:8000/students')
            .then(function (response) {
                $scope.students = response.data;
            })
            .catch(function (error) {
                console.error("Error fetching students: " + error);
            });
    };

    $scope.init();
});
