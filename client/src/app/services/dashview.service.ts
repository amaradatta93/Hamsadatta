import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import {Observable} from 'rxjs';

import { Dash } from '../models/dash';

@Injectable({
  providedIn: 'root'
})
export class DashviewService {

  constructor(private http: HttpClient) {
  }

  private dashboardUrl = 'http://127.0.0.1:8000/api/user-dashboard/posts';

  getPosts(): Observable<Dash> {
    return this.http.get<Dash>(this.dashboardUrl);
  }

}
