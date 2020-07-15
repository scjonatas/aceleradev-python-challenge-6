from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def lambda_function(request):
    question = request.data.get('question')

    if question is None:
        return Response(
            {
                "error": {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "The required property 'question' was not found in the request body"
                }
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    solution = sorted(question, reverse=True,
                      key=lambda x: (question.count(x), -question.index(x)))
    return Response({"solution": solution})
